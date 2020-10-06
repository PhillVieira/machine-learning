import * as React from "react";
import IconSvg from "../icons-svg/icons";
import { HeaderWrapper, Bar, GroupButtons, NavButton } from "./style";

export interface IHeaderProps { }

export interface IHeaderState {
  ipcRenderer?: any;
  loading: boolean;
}

export default class Header extends React.Component<
  IHeaderProps,
  IHeaderState
  > {
  private ipcRenderer?: any;

  constructor(props: IHeaderProps) {
    super(props);

    this.state = {
      ipcRenderer: null,
      loading: false,
    };
  }

  componentDidMount() {
    if (!this.state.ipcRenderer) {
      this.initializeIpcRenderer();
    }
  }

  initializeIpcRenderer = () => {
    if (!window || !window.process || !window.require) {
      throw new Error(`Unable to require renderer process`);
    }
    this.setState({
      ipcRenderer: window.require("electron").ipcRenderer,
    }, () => {
      this.state.ipcRenderer.on("reply-done-training", (event: any, args: any) => {
        console.log("HEADER", args);
        this.setState({ loading: false });
      });
    });
  };

  openTrainingMode = () => {
    const { ipcRenderer } = this.state;

    this.setState({ loading: true }, () => {
      ipcRenderer.send("open-training");
    });
  };

  openTreeTrainingMode = () => {
    const { ipcRenderer } = this.state;

    this.setState({ loading: true }, () => {
      ipcRenderer.send("open-training-tree");
    });
  };

  exitApp = () => {
    const { ipcRenderer } = this.state;
    ipcRenderer.send("close-program", "ping");
  };

  public render() {
    return (
      <HeaderWrapper>
        <Bar>Machine Learning</Bar>
        <GroupButtons>
          <NavButton
            onClick={this.openTrainingMode}
            disabled={this.state.loading}
            useMinWidth={true}
          >
            {!this.state.loading ? "Treinamento Naive Bayes" : "Em treinamento..."}
          </NavButton>
          <NavButton
            onClick={this.openTreeTrainingMode}
            disabled={this.state.loading}
            useMinWidth={true}
          >
            {!this.state.loading ? "Treinamento Árvore de Decisão" : "Em treinamento..."}
          </NavButton>
        </GroupButtons>
        <NavButton onClick={() => this.exitApp()}>
          Sair <IconSvg icon="exit" color="#fff" />{" "}
        </NavButton>
      </HeaderWrapper>
    );
  }
}
