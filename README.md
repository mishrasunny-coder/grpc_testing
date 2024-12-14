# grpc_testing
Basic gRPC testing

## To start the service
`make build`
`make run`

## To Rebuild the entire service
`make rebuild`

## To Test using grpcurl
`grpcurl -plaintext -d '{"a": 10, "b": 5}' localhost:50051 Calculator.Add`

## To Push the docker image to docker hub by tagging the latest commit sha and latest tag run
`make push`
