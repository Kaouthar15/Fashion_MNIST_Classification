import { useState } from "react";
import UploadImage from "./components/UploadImage";
import PredictionCard from "./components/PredictionCard";
import UncertaintyPanel from "./components/UncertaintyPanel";
import SamplingControl from "./components/SamplingControl";
import OODWarning from "./components/OODWarning";
import "./styles/theme.css";

function App() {
  const [result, setResult] = useState(null);
  const [nSamples, setNSamples] = useState(30);

  return (
    <div className="app-container">
      <h1 className="title">
        Bayesian Uncertainty Dashboard
      </h1>

      <div className="dashboard">
        {/* LEFT PANEL */}
        <div className="panel">
          <UploadImage setResult={setResult} nSamples={nSamples} />
          <SamplingControl
            nSamples={nSamples}
            setNSamples={setNSamples}
          />
        </div>

        {/* RIGHT PANEL */}
        <div className="panel">
          <PredictionCard result={result} />
          <UncertaintyPanel result={result} />
          <OODWarning result={result} />
        </div>
      </div>
    </div>
  );
}

export default App;