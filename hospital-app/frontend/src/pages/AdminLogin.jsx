import { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'

export default function AdminLogin() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState('')
  const [loading, setLoading] = useState(false)
  const { login, logout } = useAuth()
  const navigate = useNavigate()

  async function handleSubmit(e) {
    e.preventDefault()
    setError('')
    setLoading(true)
    try {
      const me = await login(email, password)
      if (me.role !== 'admin') {
        logout()
        setError('This portal is for administrators only.')
        return
      }
      navigate('/')
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="login-page">
      <div className="login-card">
        <div className="login-header">
          <div className="login-brand">
            <span className="brand-icon-lg">+</span>
          </div>
          <h1>Admin Portal</h1>
          <p>Administrator access only</p>
        </div>
        <form onSubmit={handleSubmit} className="login-form">
          {error && <div className="alert alert-error">{error}</div>}
          <div className="form-group">
            <label>Email</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="you@hospital.com"
              required
            />
          </div>
          <div className="form-group">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              placeholder="••••••••"
              required
            />
          </div>
          <div style={{ textAlign: 'right', marginBottom: '8px' }}>
            <Link to="/forgot-password" style={{ fontSize: '13px' }}>Forgot password?</Link>
          </div>
          <button type="submit" className="btn btn-primary btn-full" disabled={loading}>
            {loading ? 'Signing in…' : 'Sign in'}
          </button>
        </form>

        <div style={{ textAlign: 'center', marginTop: '16px', fontSize: '14px', display: 'flex', flexDirection: 'column', gap: '8px' }}>
          <p>Patient? <Link to="/login">Patient Portal</Link></p>
          <p>Doctor or Staff? <Link to="/staff-login">Staff Portal</Link></p>
        </div>
      </div>
    </div>
  )
}
