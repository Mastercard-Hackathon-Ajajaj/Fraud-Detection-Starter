# Katalog danych

Ten katalog przeznaczony jest do przechowywania danych wykorzystywanych w projekcie wykrywania oszustw.

## Struktura katalogu

```
data/
├── raw/               # Dane surowe, nieprzetworzone
├── processed/         # Dane przetworzone, gotowe do analizy
└── models/           # Zapisane modele (jeśli będą używane)
```

## Format danych

Dane powinny być przechowywane w jednym z następujących formatów:
- CSV (`.csv`)
- Excel (`.xlsx`, `.xls`)
- Parquet (`.parquet`)
- JSON (`.json`)

## Przykładowa struktura danych

Dla wykrywania oszustw, dane powinny zawierać następujące typy informacji:
- Identyfikatory transakcji
- Timestampy
- Kwoty transakcji
- Informacje o kliencie
- Informacje o merchantcie
- Lokalizacja transakcji
- Etykiety (fraud/not fraud)

## Uwagi

1. Dane wrażliwe powinny być odpowiednio zabezpieczone
2. Przed dodaniem danych do repozytorium, upewnij się, że nie zawierają one informacji poufnych
3. W przypadku dużych zbiorów danych, rozważ użycie formatu Parquet dla lepszej wydajności 