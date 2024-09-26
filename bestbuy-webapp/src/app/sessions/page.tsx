import { Session } from "../(services)/types";

export default async function SessionsPage() {
  const response = await fetch("http://0.0.0.0:80/sessions/");
  const sessions = await response.json();

  return (
    <div>
      {sessions.map((session: Session) => (
        <div key={session.id}>
          <p>{session.id}</p>
          <p>{session.scraping_started}</p>
          <p>{session.scraping_finished}</p>
          <p>{String(session.done)}</p>
        </div>
      ))}
    </div>
  );
}
