package main

import (
	"context"
	"errors"
	"log"
	"net"

	"google.golang.org/grpc"
	"google.golang.org/grpc/reflection"

	pb "grpc_test"
)

type server struct{}

const (
	port = ":50051"
)

func (s *server) OrderUpdate(ctx context.Context, in *pb.OrderItemInfo) (*pb.Acknowledgement, error) {
	log.Printf("Received request for order : %s and order item id: %s \n", in.GetOrderId(), in.GetOrderItemId())
	// write your message consumer function here that should return success and error.
	success := true
	err := errors.New("Problem in reading message")
	if success {
		return &pb.Acknowledgement{Acknowledged: success}, nil
	}
	return &pb.Acknowledgement{Acknowledged: success}, err
}

func main() {
	lis, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	s := grpc.NewServer()
	pb.RegisterCustomerOrderUpdateServer(s, &server{})
	// Register reflection service on gRPC server.
	reflection.Register(s)
	log.Println("Starting server")
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
