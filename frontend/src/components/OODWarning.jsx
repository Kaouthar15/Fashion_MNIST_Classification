export default function OODWarning({ result }) {
  if (!result || !result.is_ood) return null;

  return (
    <div className="ood-alert">
      ⚠ High Epistemic Uncertainty — Possible OOD Sample
    </div>
  );
}