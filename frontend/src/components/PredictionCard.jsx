export default function PredictionCard({ result }) {
  if (!result) return null;

  return (
    <div>
      <div className="section-title">Prediction</div>

      <h2 style={{ marginBottom: 10 }}>
        Class {result.prediction}
      </h2>

      <p style={{ opacity: 0.6 }}>
        Confidence: {(result.confidence * 100).toFixed(1)}%
      </p>
    </div>
  );
}