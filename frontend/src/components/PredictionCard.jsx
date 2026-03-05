export default function PredictionCard({ result }) {
  const empty = "—";

  const fields = [
    {
      label: "Class",
      value: result ? result.prediction : empty,
      hint: "Predicted category of the image",
      isTitle: true,
    },
    {
      label: "Confidence",
      value: result ? `${(result.confidence * 100).toFixed(1)}%` : empty,
      hint: "Probability of the predicted class",
    },
    {
      label: "Epistemic Uncertainty",
      value: result ? `${(result.mutual_information * 100).toFixed(2)}%` : empty,
      hint: "Uncertainty from lack of model knowledge",
    },
    {
      label: "Aleatoric Uncertainty",
      value: result ? `${(result.expected_entropy * 100).toFixed(2)}%` : empty,
      hint: "Uncertainty caused by noisy or ambiguous data",
    },
    {
      label: "Predictive Entropy",
      value: result ? `${(result.predictive_entropy * 100).toFixed(2)}%` : empty,
      hint: "Overall uncertainty in the prediction",
    },
    {
      label: "Calibration Error",
      value: result ? `${result.calibration_error.toFixed(4)}` : empty,
      hint: "How well confidence matches real accuracy",
    },
    {
      label: "Brier Score",
      value: result ? `${result.brier_score.toFixed(4)}` : empty,
      hint: "Error between predicted probabilities and true label",
    },
  ];

  return (
    <div>
      <div className="section-title">Prediction</div>

      {fields.map(({ label, value, isTitle, hint }) => (
        <div key={label} style={{ marginBottom: 10 }}>
          {isTitle ? (
            <>
              <h2 style={{ marginBottom: 2 }}>
                {label}: <span>{value}</span>
              </h2>
              <div style={{ fontSize: 12, opacity: 0.6 }}>{hint}</div>
            </>
          ) : (
            <>
              <p style={{ opacity: result ? 0.8 : 0.4, margin: 0 }}>
                {label}: <span style={{ fontWeight: 500 }}>{value}</span>
                {hint && result && (
                  <span
                    style={{
                      opacity: 0.5,
                      fontSize: "0.85em",
                      marginLeft: 6,
                    }}
                  >
                    ({hint})
                  </span>
                )}
              </p>
            </>
          )}
        </div>
      ))}
    </div>
  );
}