export function ReportSkeleton() {
  return (
    <div className="space-y-6 animate-fade-in">
      <div className="text-center space-y-2 mb-8">
        <div className="flex items-center justify-center gap-3 mb-4">
          <div className="h-5 w-5 rounded-full border-2 border-blue-500 border-t-transparent animate-spin" />
          <span className="text-sm" style={{ color: "var(--text-secondary)" }}>
            Analyzing competitive landscape...
          </span>
        </div>
      </div>

      {/* Executive summary skeleton */}
      <SkeletonCard lines={3} />

      {/* Competitors grid skeleton */}
      <div>
        <SkeletonHeading />
        <div className="grid gap-4 md:grid-cols-2 mt-4">
          <SkeletonCard lines={5} />
          <SkeletonCard lines={5} />
          <SkeletonCard lines={5} />
          <SkeletonCard lines={5} />
        </div>
      </div>

      {/* Market gaps skeleton */}
      <div>
        <SkeletonHeading />
        <div className="grid gap-4 md:grid-cols-2 mt-4">
          <SkeletonCard lines={4} />
          <SkeletonCard lines={4} />
        </div>
      </div>

      {/* Positioning skeleton */}
      <div>
        <SkeletonHeading />
        <div className="space-y-4 mt-4">
          <SkeletonCard lines={3} />
          <SkeletonCard lines={3} />
        </div>
      </div>
    </div>
  );
}

function SkeletonHeading() {
  return (
    <div
      className="h-6 w-48 rounded-md shimmer mb-2"
      style={{ backgroundColor: "var(--bg-surface)" }}
    />
  );
}

function SkeletonCard({ lines }: { lines: number }) {
  return (
    <div
      className="rounded-xl p-6 space-y-3 border"
      style={{
        backgroundColor: "var(--bg-surface)",
        borderColor: "var(--border-subtle)",
      }}
    >
      <div className="h-4 w-3/4 rounded shimmer" />
      {Array.from({ length: lines - 1 }).map((_, i) => (
        <div
          key={i}
          className="h-3 rounded shimmer"
          style={{ width: `${70 + Math.random() * 25}%` }}
        />
      ))}
    </div>
  );
}
