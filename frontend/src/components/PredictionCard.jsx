export default function PredictionCard({ result }) {
  const empty = "—";

  const fields = [
    {
      label: "Class",
      value: result ? result.prediction : empty,
      isTitle: true,
    },
    {
      label: "Confidence",
      value: result ? `${(result.confidence * 100).toFixed(1)}%` : empty,
    },
    {
      label: "Epistemic Uncertainty",
      value: result ? `${(result.mutual_information * 100).toFixed(2)}%` : empty,
    },
    {
      label: "Aleatoric Uncertainty",
      value: result ? `${(result.expected_entropy * 100).toFixed(2)}%` : empty,
    },
    {
      label: "Predictive Entropy",
      value: result ? `${(result.predictive_entropy * 100).toFixed(2)}%` : empty,
    },
    {
      label: "Calibration Error",
      value: result ? `${result.calibration_error.toFixed(4)}` : empty,
      hint: "lower is better",
    },
    {
      label: "Brier Score",
      value: result ? `${result.brier_score.toFixed(4)}` : empty,
      hint: "lower is better",
    },
  ];

  return (
    <div>
        <p></p>
      <div className="section-title">Prediction</div>
      {fields.map(({ label, value, isTitle, hint }) => (
        <div key={label} style={{ marginBottom: 8 }}>
          {isTitle ? (
            <h2 style={{ marginBottom: 4 }}>
              {label}: <span>{value}</span>
            </h2>
          ) : (
            <p style={{ opacity: result ? 0.8 : 0.4, margin: 0 }}>
              {label}:{" "}
              <span style={{ fontWeight: 500 }}>{value}</span>
              {hint && result && (
                <span style={{ opacity: 0.5, fontSize: "0.85em", marginLeft: 6 }}>
                  ({hint})
                </span>
              )}
            </p>
          )}
        </div>
      ))}
    </div>
  );
}