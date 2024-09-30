import { AppBar, Button, Container, Toolbar } from "@mui/material";

const pages = [
  { name: "Home", slug: "/" },
  { name: "Products", slug: "/products/" },
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
            <Button sx={{ color: "secondary.main" }} href={page.slug}>
              {page.name}
            </Button>
          ))}
        </Toolbar>
      </Container>
    </AppBar>
  );
}
