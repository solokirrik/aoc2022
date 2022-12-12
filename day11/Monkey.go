package main

const (
	oldVal           = "old"
	OpMult Operation = "*"
	OpSum  Operation = "+"
)

type Operation string

type OperationEx struct {
	Op  Operation
	Str string
	Val int64
}

func (o *OperationEx) Apply(val int64) int64 {
	opVal := o.Val
	if o.Str == oldVal {
		opVal = val
	}

	switch o.Op {
	case OpSum:
		//fmt.Println(fmt.Sprintf("oldVal %d + newVal %d", val, opVal))
		val = val + opVal
	case OpMult:
		//fmt.Println(fmt.Sprintf("oldVal %d * newVal %d", val, opVal))
		val = val * opVal
	}

	return val
}

type Monkey struct {
	ID          int64
	Activity    int64
	Items       []int64
	Op          OperationEx
	TestDivBy   int64
	TestTrueID  int64
	TestFalseID int64
}

func (m *Monkey) DoInspection(part, calmDiv int64) {
	itemVal := m.Op.Apply(m.Items[0])

	if part == 1 {
		itemVal /= calmDiv
	} else {
		itemVal %= calmDiv
	}

	//fmt.Println(fmt.Sprintf("Monkey %d: oldVal %d, newVal %d", m.ID, m.Items[0], itemVal))
	m.Items[0] = itemVal

	return
}

func (m *Monkey) Test() bool {
	return m.Items[0]%m.TestDivBy == 0
}

func (m *Monkey) ChoseToThrow() int64 {
	throwItemMonkeyID := int64(0)

	if testRes := m.Test(); testRes {
		//fmt.Println(fmt.Sprintf("Monkey %d: test Passed -> %d", m.ID, m.TestTrueID))
		throwItemMonkeyID = m.TestTrueID
	} else {
		//fmt.Println(fmt.Sprintf("Monkey %d: test Failed -> %d", m.ID, m.TestFalseID))
		throwItemMonkeyID = m.TestFalseID
	}

	return throwItemMonkeyID
}
