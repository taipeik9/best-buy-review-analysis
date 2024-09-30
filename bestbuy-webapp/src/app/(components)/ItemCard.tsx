import { Box, Typography } from "@mui/material";
import { Product, Review } from "../(assets)/types";

export default function ItemCard({ item }: { item: any }) {
  return (
    <Box
      key={item.id}
      sx={{
        bgcolor: "secondary.main",
        p: "15px",
        my: "15px",
        borderRadius: "15px",
        boxShadow: "3",
      }}
    >
      {Object.keys(item).map((key) => {
        return (
          <Typography key={`${key}${item[key]}`}>
            {key}: {item[key]}
          </Typography>
        );
      })}
    </Box>
  );
}
