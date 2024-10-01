import { Container, Typography } from "@mui/material";
import { Product } from "../(assets)/types";
import ItemCard from "../(components)/ItemCard";

export default async function ProductsPage() {
  const response = await fetch("http://0.0.0.0/products/", {
    cache: "no-store",
  });
  const products = await response.json();

  return (
    <Container>
      <Typography variant="h1">Products</Typography>
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
