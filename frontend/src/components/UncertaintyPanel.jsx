export default function UncertaintyPanel({ result }) {
  if (!result) return null;

  const bars = [
    {
      label: "Aleatoric",
      value: result.expected_entropy,
      color: "#f59e0b"
    },
    {
      label: "Epistemic",
      value: result.mutual_information,
      color: "#ef4444"
    },
    {
      label: "Predictive Entropy",
      value: result.predictive_entropy,
      color: "#22c55e"
    }
  ];

  return (
    <div style={{ marginTop: 40 }}>
      <div className="section-title">Uncertainty Decomposition</div>

      {bars.map((bar, i) => (
        <div key={i} className="bar-wrapper">
          <div className="bar-label">{bar.label}</div>
          <div className="bar-track">
            <div
              className="bar-fill"
              style={{
                width: `${bar.value * 100}%`,
                background: bar.color
              }}
            />
          </div>
        </div>
      ))}
    </div>
  );
}