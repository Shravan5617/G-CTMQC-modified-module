program potential
    IMPLICIT NONE
 
    !real*8 AA, BB,CC,DD
    !real*8 x
    !real*8 V(2,2)
  call poten_model1

contains
  subroutine poten_model1
    IMPLICIT NONE
    real*8 A,B,C,D
    real*8 x
    real*8 V(2,2)
    A=0.01d0
    B=1.6d0
    C=0.005d0
    D=1.0d0
    x=2.356d0

    if (x<0) then
      v(1,1)=-A*(1-exp(B*x))
      else if (x>0) then
      v(1,1)=A*(1-exp(-B*x))
      endif
      V(2,2)=-V(1,1)
      V(1,2)=C*exp(-D*x**2)
      V(2,1)=V(1,2)
    
       print *, x
       print *, V
  end subroutine  poten_model1
end program potential
