new Vue ({
    // ELEMENT
    el: '#app',
    
    // DATA
    data: {
      headerTitle: 'My Accounts',
      goBalance: '284.90',
      classicBalance: '1800.00',
      gBal: 0,
      cBal: 0,
      transferAmount: 0,
      msg: '',
      showMsg: false,
      msgColor: '',
      revealClass: 'slide',
      balance1: '',
      balance2: ''
    },
    
    // WATCH
    watch: {
      transferAmount: function() {
        var goAmount = parseFloat(this.goBalance);
        var classicAmount = parseFloat(this.classicBalance);
        var transAmt = parseFloat(this.transferAmount);
        if(transAmt > goAmount && this.cBal == 1) {
          this.showMessage('You have insufficient funds in your Go Account to transfer. Try a lesser amount', 'red');
        }
        if(transAmt > classicAmount && this.cBal == 2) {
          this.showMessage('You have insufficient funds in your Classic Account to transfer. Try a lesser amount', 'red');
        }
      }
    },
    
    //METHODS
    methods: {
      
      makeTransfer: function() {
        var num = 0;
        if(this.transferAmount != 0) {
          if(this.cBal == '1' && this.gBal == '1') {
            this.goBalance = this.addSum(this.goBalance, this.transferAmount, 'minus');
            this.classicBalance = this.addSum(this.classicBalance, this.transferAmount, 'add');
            num = 2;
          }
          if(this.cBal == '2' && this.gBal == '2') {
            this.goBalance = this.addSum(this.goBalance, this.transferAmount, 'add');
            this.classicBalance = this.addSum(this.classicBalance, this.transferAmount, 'minus');
            num = 1;
          }
          this.resetForm(num);
        } else {
          this.showMessage('You must enter a transfer amount', 'red');
        }
      },
      
      addSum(bal, amt, mode) {
        var b = parseFloat(bal);
        var a = parseFloat(amt);
        var sum;
        if(mode == 'minus') {
          sum = (b - a).toFixed(2);
        }
        if(mode == 'add') {
          sum = (b + a).toFixed(2);
        }
        return sum;
      },
      
      resetForm: function(num) {
        this.cBal = 0;
        this.gBal = 0;
        this.transferAmount = 0;
        this.showMessage('Tansfer Successful', 'green')
        this['balance' + num] = 'transfer-ani'
        document.getElementById('opt1').disabled = false;
        document.getElementById('opt2').disabled = false;
      },
      
      showMessage(msg, color) {
        this.showMsg = true;
        this.msg = msg;
        this.msgColor = color;
        var vm = this;
        setTimeout(function() {
          vm.showMsg = false;
        }, 2000);
      },
      
      autoSelect(num) {
        var opt1 = document.getElementById('opt1');
        var opt2 = document.getElementById('opt2');
        this.cBal = num;
        if(num == 1 || opt1.disabled == false) {
          opt2.disabled = true;
          opt1.disabled = false;
        }
        if(num == 2 || opt2.disabled == false) {
          opt1.disabled = true;
          opt2.disabled = false;
        }
      }
    }
  });