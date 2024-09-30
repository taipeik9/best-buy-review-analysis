import { Container, Typography } from "@mui/material";
import ItemCard from "../(components)/ItemCard";
import { Review } from "../(assets)/types";

export default async function Reviews() {
  const response = await fetch("http://0.0.0.0/reviews/");
  const reviews = await response.json();

  return (
    <Container>
      <Typography variant="h1">Reviews</Typography>
      {reviews.map((review: Review) => (
        <ItemCard key={review.id} item={review}></ItemCard>
      ))}
    </Container>
  );
}
