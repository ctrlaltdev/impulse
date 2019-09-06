for arch in amd64 arm32v6 arm64v8; do
  docker build -f Dockerfile.${arch} -t ctrlaltdev/impulse:${arch}-latest .
  docker push ctrlaltdev/impulse:${arch}-latest
done