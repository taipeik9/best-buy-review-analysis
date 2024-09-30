"use client";
import { useState } from "react";
import {
  Paper,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TablePagination,
  TableRow,
} from "@mui/material";
import { Column } from "../(assets)/types";
import { useRouter } from "next/navigation";

export default function BasicTable({
  columns,
  rows,
}: {
  columns: Column[];
  rows: any;
}) {
  const [page, setPage] = useState(0);
  const [rowsPerPage, setRowsPerPage] = useState(10);
  const router = useRouter();

  const handleChangePage = (
    event: React.MouseEvent<HTMLButtonElement> | null,
    newPage: number
  ) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (
    event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setRowsPerPage(parseInt(event.target.value, 10));
    setPage(0);
  };

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            {columns.map((column) => (
              <TableCell key={column.id}>{column.name}</TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {rows
            .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
            .map((row: any) => (
              <TableRow
                key={row.id}
                onClick={() => router.push(`/reviews/${row.id}`)}
                sx={{
                  "&:hover": { bgcolor: "secondary.main", cursor: "pointer" },
                }}
              >
                {columns.map((c) => (
                  <TableCell key={c.id}>{row[c.id]}</TableCell>
                ))}
              </TableRow>
            ))}
        </TableBody>
      </Table>
      <TablePagination
        component="div"
        count={100}
        page={page}
        onPageChange={handleChangePage}
        rowsPerPage={rowsPerPage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </TableContainer>
  );
}
