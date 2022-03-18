# mkamadeus-final-report

[![made-with-latex](https://img.shields.io/badge/Made%20with-LaTeX-1f425f.svg)](https://www.latex-project.org/)
[![lint](https://github.com/mkamadeus/final-report/actions/workflows/lint.yml/badge.svg)](https://github.com/mkamadeus/final-report/actions/workflows/lint.yml)
[![build](https://github.com/mkamadeus/final-report/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/mkamadeus/final-report/actions/workflows/build.yml)

## Features

This repository includes:

- My final project report made in LaTEX.
- ChkTEX workflow to lint the LaTEX report.
- Workflow to build the report and upload it to Google Drive.
- Workflow to build the report and deploy it into a Vercel webpage.

## Where can I see the report?

Check it out here: https://report.mkamadeus.dev

## Setup

### Development

To use this, install from `texlive-full` for getting all required packages.

```sh
sudo apt install texlive-full python3-pygments
```

Setup `PATH` for Pygments

Using VSCode, install some extensions for better experience:

- [VSCode LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) (for compiling LaTeX and previewing it)
- [Draw.io Integration](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio) (for making diagrams)

### CI/CD

Some things are required to be set up for the CI/CD to work. The `.github/workflows` directory can be safely be deleted if the workflows are unnecessary.

Secrets that need to be configured for uploading to Google Drive:

- `GOOGLE_CREDENTIALS` - from GCP Console, make a user credential to access the Drive API.
- `GOOGLE_FOLDER_ID` - the target Google Drive folder ID as the upload destination. Make sure your user account is invited to this folder.

Secrets that need to be configured for deploying your paper to Vercel:

- `VERCEL_ORG_ID` - Vercel organization ID, or should be your ID
- `VERCEL_PROJECT_ID` - Vercel project ID
- `VERCEL_TOKEN` - Vercel token generated for accessing your account

To get organization and project ID for the site, run this command on `web/`:

```
npx vercel link
```

## Generating PDF

### Using `Makefile`

A makefile has been provided. To compile this report into `.pdf`, use:

```sh
make
```

but it's recommended to use the extension instead.

### Using LaTeX Workshop

If you're using the [VSCode LaTeX Workshop](https://github.com/James-Yu/LaTeX-Workshop) extension, the `settings.json` file for VSCode is provided for you to use. You can run the build command provided from the extension's tab.

## Document Structure

| _for ease, this section will be written in Indonesian_

Untuk TA 1:

1. Cover
2. Cover Dalam (ditandatangani oleh pembimbing)
3. Daftar Isi
4. Daftar Gambar
5. Daftar Tabel
6. Pendahuluan
   1. Latar Belakang
   2. Rumusan Masalah
   3. Tujuan
   4. Batasan Masalah
   5. Metodologi
   6. Jadwal Pelaksanaan
7. Studi Literatur/Dasar Teori (subbab disesuaikan dengan hal-hal yang akan dibahas)
8. Rencana Penyelesaian Masalah (judul dapat disesuaikan dengan rancangan)
   1. Analisis Masalah
   2. Solusi Umum
   3. Rancangan Solusi

Untuk TA 2

1. Pendahuluan
2. Studi Literatur/Dasar Teori
3. Deskripsi Umum Solusi
   1. Analisis
   2. Perancangan
   3. Implementasi
4. Pengujian/Evaluasi Hasil
5. Kesimpulan dan Saran

disertai software, paper, poster, dll. yang menunjang sidang dan makalah.
