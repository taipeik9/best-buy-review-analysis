export default function SessionDetails({
  params,
}: {
  params: { sessionId: string };
}) {
  return <h1>Session Details {params.sessionId}</h1>;
}
