import { Container, Typography } from "@mui/material";
import { Session } from "../(assets)/types";
import ItemCard from "../(components)/ItemCard";

export default async function SessionsPage() {
  const response = await fetch("http://0.0.0.0:80/sessions/");
  const sessions = await response.json();

  return (
    <Container>
      <Typography variant="h1">Sessions</Typography>
      {sessions.map((session: Session) => (
        <ItemCard key={session.id} item={session}></ItemCard>
      ))}
    </Container>
  );
}
