# Mosaic

Create a multispectral mosaic from compatible georeferenced images. Supply STAC Items through the GUI catalog selection or configure a metadata_in provider in this one workflow file. Inputs need known radiometry/units, matching band order and radiometry. The first step aligns images to EPSG:6933; set `process.align_grid.crs` and its resolution for your area and intended output. Add radiometric correction plugins if necessary. The workflow selects alignment, footprint extraction, footprint cleaning, Voronoi seamlines, per-scene masking, and mosaicking. The solver assembles their data dependencies. Install the plugins and their GDAL, spectralmatch and geopandas requirements before execution.

Nothing is saved by default. Enable `process.mosaic.outputs.result.save` to use the mosaic plugin's default output path, or override `data_out.settings.path`. Enable saving on intermediate results independently. Goals express the desired mosaic state; they never specify files to download.
