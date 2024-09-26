import { Session, Review } from "../../(services)/types";

export default async function SessionDetails({
  params,
}: {
  params: { sessionId: string };
}) {
  const response = await fetch(
    `http://0.0.0.0:80/sessions/${params.sessionId}/reviews/`
  );
  const reviews = await response.json();

  return (
    <>
      <h1>Session Details {params.sessionId}</h1>
      <h2>Reviews:</h2>
      {reviews.map((review: Review) => (
        <div key={review.id}>
          <p>{review.id}</p>
          <p>{review.rating}</p>
          <p>{review.title}</p>
          <p>{review.content}</p>
        </div>
      ))}
    </>
  );
}
