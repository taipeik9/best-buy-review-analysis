import { Product } from "../(services)/types";

export default async function ProductsPage({
  params,
}: {
  params: { productId: string };
}) {
  const response = await fetch("http://0.0.0.0/products/");
  const products = await response.json();

  return (
    <>
      <h1>Products {params.productId}</h1>
      {products.map((product: Product) => (
        <div key={product.id}>
          <p>{product.id}</p>
          <p>{product.title}</p>
          <p>{product.short_description}</p>
          <p>{product.avg_rating}</p>
          <p>{product.sale_price}</p>
          <p>{product.regular_price}</p>
        </div>
      ))}
    </>
  );
}
