> Reconstructed archive, assembled 2026-09-29. March 2024 author dates are assigned for this edition, not recovered original work timestamps.

# Synthetic area summarizer

Run `python examples/summarize_areas.py`. No external packages are required. Expected output: three features, 400 square metres of invented area, with 75% example grassland and 25% example woodland.

Percentages use the sum of supplied feature areas, not a surveyed site boundary. The example cannot detect overlaps, gaps, coordinate-system errors, or misclassified habitats. Use ordinary finite numeric scales; this is a small teaching example rather than a production GIS validator. Its outputs are not research findings about the farm.
