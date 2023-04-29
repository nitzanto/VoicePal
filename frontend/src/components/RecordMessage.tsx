import { ReactMediaRecorder } from "react-media-recorder";
import RecordIcon from "./RecordIcon";

type Props = {
  handleStop: any; //Function
};


//Prebuilt Recorder for browser in React
function RecordMessage({ handleStop }: Props) {
  return (
    <ReactMediaRecorder
      audio
      onStop={handleStop}
      render={({ status, startRecording, stopRecording }) => (
        <div className="mt-2">
          <button
            onMouseDown={startRecording}
            onMouseUp={stopRecording}
            className="bg-white p-4 rounded-full"
          ><RecordIcon classText={status=="recording" ? "animate-pulse text-red-500" : "text-sky-500"} /></button>
          <p className="mt-2 text-white font-light">{status}</p>
        </div>
      )} // Returns JSX
    />
  );
}

export default RecordMessage;
