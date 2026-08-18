import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Sunday to Sunday — Design System',
  description: 'Component library and visual identity for Sunday to Sunday projects.',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="h-full antialiased">
      <body className="min-h-full flex flex-col">{children}</body>
    </html>
  )
}
