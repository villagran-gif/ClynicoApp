// src/app/layout.tsx
import type { Metadata } from 'next';
import './globals.css'; // quítala si no tienes este archivo

export const metadata: Metadata = {
  title: {
    default: 'ClynicoApp',
    template: '%s · ClynicoApp',
  },
  description: 'Asistente bariátrico Clynico',
  manifest: '/manifest.webmanifest',
  themeColor: '#0071b8',
  icons: {
    icon: '/icons/icon-192.png',
    apple: '/icons/apple-touch-icon.png',
  },
  // iOS: abrir como app a pantalla completa y estilo de barra
  appleWebApp: {
    capable: true,
    statusBarStyle: 'black-translucent',
    title: 'ClynicoApp',
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="es">
      <body>{children}</body>
    </html>
  );
}
