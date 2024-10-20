import React from "react";
import Background from "../images/background-bm.jpg";
import { Typography, Divider, Grid2 as Grid } from "@mui/material";
import "./App.css";

export default function App() {
  return (
    <div className="App">
      <div>
        <img src={Background} className="background-header" alt="background" />
        <div className="nav-bar-header">
          <Typography
            variant="h4"
            id="text-nav"
            sx={{ fontFamily: "The Seasons, Arial, sans-serif" }}
          >
            <a href="./" id="link-text">
              Home
            </a>
          </Typography>
          <Typography
            variant="h4"
            id="text-nav"
            sx={{ fontFamily: "The Seasons, Arial, sans-serif" }}
          >
            <a href="./" id="link-text">
              Beat Match
            </a>
          </Typography>
          <Typography variant="h4" id="text-nav" sx={{ fontFamily: "The Seasons, Arial, sans-serif" }}>
            <a href="./documentsPage" id="link-text">
              Documentação
            </a>
          </Typography>
        </div>
        <Divider id="divisor" />
      </div>
      <div>
        <Divider id="divisor-01" />
        <Divider id="divisor-02" />
      </div>
      <div>
        <Divider id="divisor-03" />
        <Divider id="divisor-04" />
      </div>
      <Grid container className="main-content">
        <Grid container className="content-left">
          <Typography
            variant="h5"
            sx={{ fontFamily: "The SeasonsN, Arial, sans-serif" }}
            fontWeight="normal"
          >
            <Typography
              variant="h3"
              sx={{ fontFamily: "The Seasons, Arial, sans-serif", mb: 2 }}
            >
              Beat Match
            </Typography>
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Gerenciamento
            </Typography>
            Denis Filho Cunha Godoi <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Back-End
            </Typography>
            Denis Filho Cunha Godoi <br />
            Vitor Hugo Neves Do Vale Camargos <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Front-End
            </Typography>
            Denis Filho Cunha Godoi <br />
            Luciano Henrique Medeiros Natividade Santos
            <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Documentação
            </Typography>
            Vitor Hugo Rodrigues Machado
            <br />
            Antônio Carlos Camargo Fernandes
            <br />
            Edson Diniz Ferreira Neto
            <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 1,
                mt: 2,
              }}
            >
              Design
            </Typography>
            Denis Filho Cunha Godoi
          </Typography>
        </Grid>
        <Grid container className="content-right">
          <Typography
            variant="h5"
            sx={{ fontFamily: "The SeasonsN, Arial, sans-serif" }}
          >
            <Typography
              variant="h3"
              sx={{ fontFamily: "The Seasons, Arial, sans-serif", mb: 2 }}
            >
              Quick Match
            </Typography>
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Gerenciamento
            </Typography>
            Murilo Ferreira Borges <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Codígo
            </Typography>
            Murilo Ferreira Borges <br />
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Produção
            </Typography>
            Murilo Ferreira Borges
            <Typography
              variant="h4"
              sx={{
                fontFamily: "The Seasons, Arial, sans-serif",
                mb: 2,
                mt: 2,
              }}
            >
              Documentação
            </Typography>
            Murilo Ferreira Borges
            <br />
          </Typography>
        </Grid>
      </Grid>
      <div>
        <img src={Background} className="background-footer" alt="logo" />
      </div>
    </div>
  );
}
