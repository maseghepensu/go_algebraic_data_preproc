python go_test1.py prog0.go > prog0_quasi-ok.go
go fmt prog0_quasi-ok.go
go build prog0_quasi-ok.go
prog0_quasi-ok.exe
