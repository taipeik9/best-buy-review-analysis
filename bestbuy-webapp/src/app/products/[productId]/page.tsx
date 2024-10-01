import { Column, Product, Review } from "@/app/(assets)/types";
import BasicTable from "@/app/(components)/BasicTable";
import ItemCard from "@/app/(components)/ItemCard";
import { Container, Typography } from "@mui/material";

const columns: Column[] = [
  { name: "ID", id: "id" },
  { name: "Rating", id: "rating" },
  { name: "Title", id: "title" },
  { name: "Date", id: "date" },
];

export default async function ProductDetails({
  params,
}: {
  params: { productId: string };
}) {
  const productResponse = await fetch(
    `http://0.0.0.0:80/products/${params.productId}/`
  );
  const product: Product = await productResponse.json();

  const reviewResponse = await fetch(
    `http://0.0.0.0:80/products/${params.productId}/reviews/`,
    { cache: "no-store" }
  );
  const reviews = await reviewResponse.json();

  const fetchMoreData = async (skip: number) => {
    "use server";
    const response = await fetch(
      `http://0.0.0.0:80/products/${params.productId}/reviews/?skip=${skip}`,
      { cache: "no-store" }
    );
    const reviews = await response.json();

    return reviews.data;
  };

  return (
    <Container>
      <Typography variant="h1">Product Details: {product.id}</Typography>
      <ItemCard item={product}></ItemCard>
      <Typography variant="h2">Reviews</Typography>
      <BasicTable
        columns={columns}
        rows={reviews.data}
        total={reviews.total}
        fetchMoreData={fetchMoreData}
      />
    </Container>
  );
}
