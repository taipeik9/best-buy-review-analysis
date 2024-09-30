"use client";
import { Box, Button, Container, TextField, Typography } from "@mui/material";
import { useState } from "react";
import { Session } from "./(assets)/types";
import ItemCard from "./(components)/ItemCard";

export default function Home() {
  const [query, setQuery] = useState<string | null>(null);
  const [session, setSession] = useState<Session | null>(null);

  const handleSearch = async () => {
    if (query) {
      const scrapeResponse = await fetch(
        `http://0.0.0.0:80/scrape/${encodeURIComponent(query)}/`,
        { method: "POST" }
      );
      const scrapeResponseJson = await scrapeResponse.json();

      const sessionResponse = await fetch(
        `http://0.0.0.0:80/sessions/${scrapeResponseJson.session_id}/`
      );
      const session: Session = await sessionResponse.json();
      setSession(session);
    }
  };

  return (
    <Container>
      <Typography variant="h1">Best Buy Review Webscraper</Typography>
      <Typography>
        Type a query and click on the scrape button to send a webscraping
        request to the API
      </Typography>
      <Box
        sx={{
          display: "flex",
          width: "100%",
          height: "100%",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <TextField
          id="query"
          label="Query"
          variant="outlined"
          sx={{ my: "15px" }}
          onChange={(e) => {
            setQuery(e.target.value);
          }}
        />
        <Button
          variant="contained"
          sx={{ mx: "15px", p: "15px" }}
          onClick={handleSearch}
        >
          Scrape
        </Button>
      </Box>

      {session && (
        <Box>
          <Typography>Scraping has started</Typography>
          <ItemCard item={session} href={`/sessions/${session.id}`}></ItemCard>
        </Box>
      )}
    </Container>
  );
}
