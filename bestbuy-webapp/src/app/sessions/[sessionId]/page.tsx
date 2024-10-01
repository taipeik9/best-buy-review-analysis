import { Product, Session } from "@/app/(assets)/types";
import ItemCard from "@/app/(components)/ItemCard";
import { Container, Typography } from "@mui/material";

export default async function ProductDetails({
  params,
}: {
  params: { sessionId: string };
}) {
  const sessionResponse = await fetch(
    `http://0.0.0.0:80/sessions/${params.sessionId}/`,
    { cache: "no-store" }
  );
  const session: Session = await sessionResponse.json();

  const reviewResponse = await fetch(
    `http://0.0.0.0:80/sessions/${params.sessionId}/products/`,
    { cache: "no-store" }
  );
  const products: Product[] = await reviewResponse.json();

  return (
    <Container>
      <Typography variant="h1">Session Details</Typography>
      <ItemCard item={session}></ItemCard>
      <Typography variant="h2">Products</Typography>
      {products.map((product: Product) => (
        <ItemCard
          key={product.id}
          item={product}
          href={`/products/${product.id}`}
        />
      ))}
    </Container>
  );
}
