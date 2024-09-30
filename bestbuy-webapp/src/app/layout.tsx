import { Roboto } from "next/font/google";
import { theme } from "./(assets)/theme";
import { ThemeProvider } from "@mui/material";
import NavBar from "./(components)/NavBar";

export const metadata = {
  title: "WebScraper - Best Buy",
  description: "Webscraper for Best Buy reviews.",
};

const roboto = Roboto({
  weight: ["300", "400", "500", "700"],
  subsets: ["latin"],
  display: "swap",
  variable: "--font-roboto",
});

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={roboto.variable} style={{ margin: 0 }}>
        <ThemeProvider theme={theme}>
          <NavBar />
          {children}
        </ThemeProvider>
      </body>
    </html>
  );
}
