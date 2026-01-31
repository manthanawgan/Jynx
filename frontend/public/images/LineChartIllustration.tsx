import type { SVGProps } from "react"

export const LineChartIllustration = (props: SVGProps<SVGSVGElement>) => (
  <svg
    viewBox="0 0 980 328"
    xmlns="http://www.w3.org/2000/svg"
    fill="none"
    {...props}
  >
    {/* Background */}
    <rect width="980" height="328" fill="#F9FAFB" />
    
    {/* Title */}
    <text x="490" y="40" textAnchor="middle" fontSize="24" fontWeight="bold" fill="#111827">
      Station Performance
    </text>
    
    {/* Table Header Background */}
    <rect x="40" y="70" width="900" height="50" fill="#374151" rx="6" />
    
    {/* Table Headers */}
    <text x="70" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Station</text>
    <text x="340" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Sessions</text>
    <text x="490" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Avg Wait</text>
    <text x="640" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Power Limited</text>
    <text x="780" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Emergencies</text>
    <text x="870" y="102" fontSize="14" fontWeight="600" fill="#FFFFFF">Grid Impact</text>
    
    {/* Row 1 - Central Mall Hub */}
    <rect x="40" y="120" width="900" height="60" fill="#FFFFFF" stroke="#E5E7EB" strokeWidth="1" />
    <text x="70" y="155" fontSize="15" fill="#111827" fontWeight="500">Central Mall Hub</text>
    <text x="370" y="155" fontSize="15" fill="#111827">312</text>
    <text x="515" y="155" fontSize="15" fill="#111827">8 min</text>
    <text x="680" y="155" fontSize="15" fill="#111827">Yes</text>
    <text x="810" y="155" fontSize="15" fill="#111827">4</text>
    <text x="880" y="155" fontSize="15" fill="#10B981" fontWeight="600">Stable</text>
    
    {/* Row 2 - Riverside Apartments */}
    <rect x="40" y="180" width="900" height="60" fill="#F9FAFB" stroke="#E5E7EB" strokeWidth="1" />
    <text x="70" y="215" fontSize="15" fill="#111827" fontWeight="500">Riverside Apartments</text>
    <text x="370" y="215" fontSize="15" fill="#111827">184</text>
    <text x="515" y="215" fontSize="15" fill="#111827">12 min</text>
    <text x="680" y="215" fontSize="15" fill="#111827">Yes</text>
    <text x="810" y="215" fontSize="15" fill="#111827">2</text>
    <text x="880" y="215" fontSize="15" fill="#10B981" fontWeight="600">Stable</text>
    
    {/* Row 3 - Tech Park Garage */}
    <rect x="40" y="240" width="900" height="60" fill="#FFFFFF" stroke="#E5E7EB" strokeWidth="1" />
    <text x="70" y="275" fontSize="15" fill="#111827" fontWeight="500">Tech Park Garage</text>
    <text x="370" y="275" fontSize="15" fill="#111827">266</text>
    <text x="515" y="275" fontSize="15" fill="#111827">6 min</text>
    <text x="680" y="275" fontSize="15" fill="#111827">No</text>
    <text x="810" y="275" fontSize="15" fill="#111827">1</text>
    <text x="880" y="275" fontSize="15" fill="#3B82F6" fontWeight="600">Optimal</text>
  </svg>
)