# mkamadeus-final-report

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![lint](https://github.com/mkamadeus/final-report/actions/workflows/lint.yml/badge.svg)](https://github.com/mkamadeus/final-report/actions/workflows/lint.yml)
[![build](https://github.com/mkamadeus/final-report/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mkamadeus/final-report/actions/workflows/build.yml)

## Features

This repository includes:
- My final project report made in LaTEX.
- ChkTEX workflow to lint the LaTEX report.
- Workflow to build the report and upload it to Google Drive.

## Setup

To use this, install from `texlive-full` for easier dependencies management.

```sh
sudo apt install texlive-full
```

## Generating PDF

### Using `Makefile`

A makefile has been provided. To compile this report into `.pdf`, use:

```sh
make
```

### Using Latex Workshop

If you're using the [VSCode Latex Workshop](https://github.com/James-Yu/LaTeX-Workshop) extension, the `settings.json` file for VSCode is provided for you to use. You can run the build command provided from the extension's tab.

## Additional Notes

My final project notes:
https://docs.google.com/document/d/1ruI1CTkQI1rTCbM2XpxtThPhjFf4rjzOTXHYHvPGUDc/

## Table of Contents

For TA1:
1. Pendahluan
2. Studi Literatur/Dasar Teori
3. Deskripsi Umum Solusi (Ide Umum penyelesaian masalah, hasil analisis 50%)

For TA2:
1. Pendahluan
2. Studi Literatur/Dasar Teori
3. Deskripsi Umum Solusi
    1. Analisis
    2. Peracangan
    3. Implementasi
4. Pengujian/Evaluasi Hasil
5. Kesimpulan dan Saran

+ additional software, paper, poster, etc.