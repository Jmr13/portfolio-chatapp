"use client";

import useMousePosition from "@/hooks/useMousePosition";
import { useEffect, useState } from "react";

export default function EyeWatch() {
  const { x, y } = useMousePosition();

  const eyeX = 150;
  const eyeY = 100;
  const IRIS_MAX = 12;
  const PUPIL_MAX = 18;

  const [isEyeOpen, setIsEyeOpen] = useState(true);
  const [iris, setIris] = useState({ x: eyeX, y: eyeY });
  const [pupil, setPupil] = useState({ x: eyeX, y: eyeY });

  useEffect(() => {
    if (!isEyeOpen || x == null || y == null) return;

    const dx = (x / window.innerWidth) * 2 - 1;
    const dy = (y / window.innerHeight) * 2 - 1;

    setIris({ x: eyeX + dx * IRIS_MAX, y: eyeY + dy * IRIS_MAX });
    setPupil({ x: eyeX + dx * PUPIL_MAX, y: eyeY + dy * PUPIL_MAX });
  }, [x, y, isEyeOpen]);

  const OPEN_PATH = "M 50 100 Q 150 30 250 100 Q 150 170 50 100 Z";
  const CLOSED_PATH = "M 50 100 Q 150 100 250 100 Q 150 100 50 100 Z";

  return (
    <svg
      className="fixed top-0 left-0 w-full h-full pointer-events-none -z-10"
      viewBox="0 0 300 200"
    >
      <clipPath id="eyeClip">
        <path fill="white" stroke="none" d={isEyeOpen ? OPEN_PATH : CLOSED_PATH} />
      </clipPath>

      <path
        fill="white"
        stroke="black"
        strokeWidth={2}
        d={isEyeOpen ? OPEN_PATH : CLOSED_PATH}
      />

      {isEyeOpen && (
        <g clipPath="url(#eyeClip)">
          <circle cx={iris.x} cy={iris.y} r="30" fill="none" stroke="black" strokeWidth="2" />
          <circle cx={pupil.x} cy={pupil.y} r="15" fill="black" />
        </g>
      )}
    </svg>
  );
}