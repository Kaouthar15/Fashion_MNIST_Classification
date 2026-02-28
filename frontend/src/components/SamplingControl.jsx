export default function SamplingControl({ nSamples, setNSamples }) {
  return (
    <div style={{ marginTop: 40 }}>
      <div className="section-title">Stochastic Inference</div>

      <input
        type="range"
        min="5"
        max="100"
        value={nSamples}
        onChange={(e) => setNSamples(Number(e.target.value))}
      />

      <p style={{ marginTop: 10, opacity: 0.5 }}>
        {nSamples} Monte Carlo passes
      </p>
    </div>
  );
}