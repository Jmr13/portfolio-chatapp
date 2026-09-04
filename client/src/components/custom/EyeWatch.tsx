"use client";

import useMousePosition from "@/hooks/useMousePosition";
import { useEffect, useId, useState } from "react";

export default function EyeWatch() {
  const { x, y } = useMousePosition();
  const clipPathId = useId();

  const eyeX = 150;
  const eyeY = 100;
  const IRIS_MAX = 12;
  const PUPIL_MAX = 18;

  const [iris, setIris] = useState({ x: eyeX, y: eyeY });
  const [pupil, setPupil] = useState({ x: eyeX, y: eyeY });

  useEffect(() => {
    const dx = (x / window.innerWidth) * 2 - 1;
    const dy = (y / window.innerHeight) * 2 - 1;

    setIris({ x: eyeX + dx * IRIS_MAX, y: eyeY + dy * IRIS_MAX });
    setPupil({ x: eyeX + dx * PUPIL_MAX, y: eyeY + dy * PUPIL_MAX });
  }, [x, y]);

  const OPEN_PATH = "M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z";

  return (
    <svg
      className="fixed top-0 left-0 w-full h-full pointer-events-none -z-10"
      viewBox="0 0 300 200"
    >
      <clipPath id={clipPathId}>
        <path fill="white" stroke="none" d={OPEN_PATH} />
      </clipPath>

      <path
        fill="white"
        stroke="black"
        strokeWidth={2}
        d={OPEN_PATH}
      />

      <g clipPath={`url(#${clipPathId})`}>
        <circle cx={iris.x} cy={iris.y} r="30" fill="none" stroke="black" strokeWidth="2" />
        <circle cx={pupil.x} cy={pupil.y} r="15" fill="black" />
      </g>
    </svg>
  );
}