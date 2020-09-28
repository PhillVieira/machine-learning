import styled from "styled-components";

const primary = "#8FBB";

export const HeaderWrapper = styled.div`
  display: flex;
  justify-content: space-between;
  align-content: top;
  height: 60px;
  padding: 24px 6px 0px 6px;
  width: 100%;
  color: ${primary};
  background-color: #282c34;
  border-bottom: 1px solid ${primary};
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
`;

export const Bar = styled.div`
  background-color: rgba(0, 0, 0, 0.2);
  position: absolute;
  top: 0;
  left: 0;
  color: #8fbb;
  height: 16px;
  padding: 2px 10px;
  width: 100%;
  font-size: 10px;
  cursor: grab;
  -webkit-app-region: drag;
`;

export const GroupButtons = styled.div`
  display: flex;
  width: 200px;
  justify-content: space-around;
`;

export const NavButton = styled.button`
  display: block;
  font-weight: 500;
  padding: 4px 10px;
  line-height: 26px;
  font-size: 13px;
  color: ${primary};
  cursor: pointer;
  transition: all 0.2s ease-in-out;
  border-radius: 4px 4px 0px 0px;
  text-transform: uppercase;
  background: none;
  min-width: ${(props: NavButtonProps) => props.useMinWidth && "200px"};

  &:disabled {
    color: #000000;
    background: #999999;
    cursor: not-allowed;
  }

  &:hover {
    background-color: ${primary};
    color: #282c34;

    /* SVG HOVER COLOR */
    svg > g {
      fill: #282c34;
    }
  }
`;

export interface NavButtonProps {
  useMinWidth?: boolean;
}
