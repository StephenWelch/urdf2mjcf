from distutils.core import setup

setup(
    version="2.0.4",
    scripts=["scripts/urdf2mjcf"],
    packages=["urdf2mjcf"],
    package_dir={"": "src"},
)
