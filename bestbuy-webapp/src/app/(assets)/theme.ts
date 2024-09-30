"use client";
import { createTheme } from "@mui/material";

export const theme = createTheme({
  palette: {
    primary: {
      main: "#3364cc",
    },
    secondary: {
      main: "#f0f0f5",
      dark: "#89898f",
    },
  },
  typography: {
    fontFamily: "var(--font-roboto)",
    h1: {
      fontSize: "3em",
      fontWeight: 700,
    },
    h2: {
      fontSize: "2em",
      fontWeight: 500,
    },
    h3: {
      fontSize: "1em",
      fontWeight: 300,
    },
  },
});
