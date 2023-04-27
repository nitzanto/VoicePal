import { useState } from "react";
import Title from "./Title";

function Controller() {
  const [isLoading, setIsLoading] = useState(false); // isLoading state
  const [messages, setMessages] = useState<any[]>([]); //messages array

  const createBlobUrl = (data: any) => {};

  const handleStop = async () => {}; //async axios, if user clicked to stop recording

  return (
    <div className="h-screen overflow-y-hidden">
      <Title setMessages={setMessages} />
      <div className="flex flex-col justify-between h-full overflow-y-scroll pb-96">
        {/* Recorder */}
        <div className="fixed bottom-0 w-full py-6 border-t text-center bg-gradient-to-r from-sky-500 to-green-500 ">
          <div className="flex justify-center items-center w-full">
            <div>Recorder</div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Controller;
