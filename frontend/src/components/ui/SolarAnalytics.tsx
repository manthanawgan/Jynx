import {
  RiDropFill,
  RiNavigationFill,
  RiPieChartFill,
  RiRobot3Fill,
} from "@remixicon/react"
import { Divider } from "../Divider"
import AnalyticsIllustration from "./AnalyticsIllustration"
import { StickerCard } from "./StickerCard"

export function SolarAnalytics() {
  return (
    <section
      aria-labelledby="solar-analytics"
      className="relative mx-auto w-full max-w-6xl overflow-hidden"
    >
      <div>
        <h2
          id="solar-analytics"
          className="relative scroll-my-24 text-lg font-semibold tracking-tight text-orange-500"
        >
          Jynx-ev Analytics
          <div className="absolute top-1 -left-[8px] h-5 w-[3px] rounded-r-sm bg-orange-500" />
        </h2>
        <p className="mt-2 max-w-lg text-3xl font-semibold tracking-tighter text-balance text-gray-900 md:text-4xl">
        Turn charging data into grid-safe growth.
        </p>
      </div>
      <div className="*:pointer-events-none">
        <AnalyticsIllustration />
      </div>
      <Divider className="mt-0"></Divider>
      <div className="grid grid-cols-1 grid-rows-2 gap-6 md:grid-cols-4 md:grid-rows-1">
        <StickerCard
          Icon={RiNavigationFill}
          title="Dynamic Slot Scheduling"
          description="AI-driven algorithms fairly distribute charging time based on demand, battery state, and grid constraints."
        />
        <StickerCard
          Icon={RiRobot3Fill}
          title="Emergency Verification"
          description="Real-time vehicle telemetry ensures priority is granted only when truly needed."
        />
        <StickerCard
          Icon={RiDropFill}
          title="Fleet Integration"
          description="Public transport, logistics, and emergency fleets connect via secure APIs for coordinated charging."
        />
        <StickerCard
          Icon={RiPieChartFill}
          title="Load-Aware Throttling"
          description="Automatically reduce or boost charger power to prevent transformer overloads."
        />
      </div>
    </section>
  )
}
