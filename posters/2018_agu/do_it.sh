gs \
    -dCompatibilityLevel=1.5 \
    -dSubsetFonts=true \
    -o output.pdf \
    -sDEVICE=pdfwrite \
    -dNOPAUSE \
    -dBATCH \
    -dColorConversionStrategy=/LeaveColorUnchanged \
    -dDownsampleMonoImages=false \
    -dDownsampleGrayImages=false \
    -dDownsampleColorImages=false \
    -dAutoFilterColorImages=false \
    -dAutoFilterGrayImages=false \
    -dColorImageFilter=/FlateEncode \
    -dGrayImageFilter=/FlateEncode \
    AGU_2016_ObsPy.pdf
