import * as React from "react";
import Timer from 'react-compound-timer'

export interface ITimerProps {
  done?: boolean
}

const TimerLoading: React.FC<ITimerProps> = ({ done }) => {


  return (
    <div style={{ display: 'block', width: '100%', textAlign: 'center', color: '#999' }}>
      <span>Tempo de treino - </span>
      <Timer formatValue={(value) => `${(value < 10 ? `0${value}` : value)} `}>
        {({ start, stop }: { start: any, stop: any }) => (
          < React.Fragment  >
            {done ? stop() : start()}
            <Timer.Hours formatValue={value => `${value}:`} />
            <Timer.Minutes formatValue={value => `${value}:`} />
            <Timer.Seconds formatValue={value => `${value}`} />
          </React.Fragment>
        )
        }
      </Timer >
    </div>
  );

}
export default TimerLoading;
