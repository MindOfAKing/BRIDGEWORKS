import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "BRIDGEWORKS — Competitive Intelligence for Entrepreneurs",
  description:
    "Analyze your market, identify competitors, uncover gaps, and find your positioning edge — powered by AI.",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="min-h-screen" style={{ backgroundColor: "var(--bg-base)" }}>
        {children}
      </body>
    </html>
  );
}
