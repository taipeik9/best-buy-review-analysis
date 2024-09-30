import { AppBar, Container, Toolbar, Typography } from "@mui/material";

const pages = [
  { name: "Home", slug: "/" },
  { name: "Products", slug: "/products/" },
  { name: "Reviews", slug: "/reviews/" },
  { name: "Sessions", slug: "/sessions/" },
];

export default function NavBar() {
  return (
    <AppBar
      position="static"
      sx={{ boxShadow: "none", marginBlockEnd: "15px" }}
    >
      <Container>
        <Toolbar disableGutters>
          {pages.map((page) => (
            <Typography
              key={page.name}
              component="a"
              href={page.slug}
              sx={{
                mr: "50px",
                fontWeight: 700,
                color: "inherit",
                textDecoration: "none",
              }}
            >
              {page.name}
            </Typography>
          ))}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
