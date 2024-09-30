import { Box, Button, Typography } from "@mui/material";

export default function ItemCard({ item, href }: { item: any; href?: string }) {
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
            {key}: {`${item[key]}`}
          </Typography>
        );
      })}
      {href && (
        <Button variant="outlined" href={href}>
          View Details
        </Button>
      )}
    </Box>
  );
}
