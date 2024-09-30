import ItemCard from "@/app/(components)/ItemCard";
import { Container, Typography } from "@mui/material";

export default async function ReviewDetailsPage({
  params,
}: {
  params: { reviewId: string };
}) {
  const response = await fetch(`http://0.0.0.0:80/reviews/${params.reviewId}/`);
  const review = await response.json();

  return (
    <Container>
      <Typography variant="h1">Review Details</Typography>
      <ItemCard item={review} />
    </Container>
  );
}
