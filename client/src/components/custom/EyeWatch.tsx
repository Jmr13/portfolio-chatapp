export default function EyeWatch() {
  return (
    <svg
      className="fixed top-0 left-0 w-full h-full pointer-events-none -z-10"
      viewBox="0 0 300 200"
    >
      <clipPath id="eyeClip">
        <path fill="white" stroke="none">
          <animate
            attributeName="d"
            dur="2s"
            repeatCount="indefinite"
            values="             
            M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z;             
            M 50 100 Q 150 100 250 100 Q 150 100 50 100 Z;             
            M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z"
            keyTimes="0; 0.5; 1"
            calcMode="spline"
            keySplines="0.4 0 1 1; 0 0 0.2 1"
          />
        </path>
      </clipPath>
      <path fill="white" stroke="black" strokeWidth={2}>
        <animate
          attributeName="d"
          dur="2s"
          repeatCount="indefinite"
          values="           
          M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z;           
          M 50 100 Q 150 100 250 100 Q 150 100 50 100 Z;           
          M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z"
          keyTimes="0; 0.5; 1"
          calcMode="spline"
          keySplines="0.4 0 1 1; 0 0 0.2 1"
        />
      </path>
      <g clipPath="url(#eyeClip)">
        <circle cx="150" cy="100" r="30" fill="none" stroke="black" strokeWidth="2" />
        <circle cx="150" cy="100" r="10" fill="none" stroke="black" strokeWidth="2" />
      </g>
    </svg>
  )
}